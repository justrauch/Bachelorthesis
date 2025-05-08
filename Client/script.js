const dropZone = document.getElementById('dropZone');
const submitBtn1 = document.getElementById('submitBtn1');
const submitBtn2 = document.getElementById('submitBtn2');
const submitBtn3 = document.getElementById('submitBtn3');

function switchsite(page) {
    for (let i = 1; i <= 3; i++) {
      const tmp = document.getElementById('page' + i);
      tmp.style.display = (i === page) ? 'block' : 'none';
      if(i == 3){
        document.getElementById("submitBtn3").click();
      }
    }
}

function enableButtonIfFilesPresent(dropZone, count) {
    const button = dropZone.parentElement.querySelector('button');
    if (button) {
        button.disabled = count === 0;
    }
}

function showFilePreview(dropZone, files) {
    dropZone.innerHTML = '';
    const filePreview = document.createElement("div");
    filePreview.className = "filePreview";
  
    const file = files[0];
    dropZone.file = file;
    const info = document.createElement('div');
    info.style.marginBottom = '16px';
  
    const text = document.createElement('div');
    text.textContent = `Dateiname: ${file.name} (${file.type || 'Unbekannter Typ'})`;
  
    info.appendChild(text);
    filePreview.appendChild(info);
    dropZone.appendChild(filePreview);
  }

document.querySelectorAll('.drop-zone').forEach((dropZone) => {
    dropZone.addEventListener('dragover', (e) => {
      e.preventDefault();
      dropZone.classList.add('dragover');
    });
  
    dropZone.addEventListener('dragleave', () => {
      dropZone.classList.remove('dragover');
    });
  
    dropZone.addEventListener('drop', (e) => {
      e.preventDefault();
      dropZone.classList.remove('dragover');
      const files = e.dataTransfer.files;
      enableButtonIfFilesPresent(dropZone, files.length);
      showFilePreview(dropZone, files);
    });
  
    dropZone.addEventListener('click', () => {
      const fileInput = document.createElement('input');
      fileInput.type = 'file';
      fileInput.multiple = true;
      fileInput.onchange = () => {
        enableButtonIfFilesPresent(dropZone, fileInput.files.length);
        showFilePreview(dropZone, fileInput.files);
      };
      fileInput.click();
    });
  });

  submitBtn1.addEventListener('click', () => {
    const file = document.querySelector("#page1 .drop-zone").file;
  
    if (
      file.type === "application/x-zip-compressed" ||
      file.type === "application/zip" ||
      file.name.toLowerCase().endsWith(".zip")
    ) {
      const formData = new FormData();
      formData.append("file", file);
  
      fetch("http://localhost:8000/api/process-zip", {
        method: "POST",
        headers: {
          "Accept": "application/zip"
        },
        body: formData
      })
      .then(response => {
        if (response.status === 429) {
          alert("Verarbeitung ist aktuell belegt. Bitte versuche es in wenigen Minuten erneut.");
          throw new Error("Prozess belegt");
        }
        if (!response.ok) {
          throw new Error("Unbekannter Fehler beim Hochladen.");
        }
        switchsite(3);
        document.getElementById("submitBtn3").click();
      })
      .catch(error => console.error("Status-Abfrage fehlgeschlagen:", error));
  
    } else {
      alert("Bitte wählen Sie eine ZIP-Datei aus, um fortzufahren.");
    }
  });
  

  submitBtn3.addEventListener('click', () => {
    submitBtn3.style.display = "none";

    const table = document.getElementById("page3table");
    let interval = setInterval(() => {
        fetch("http://localhost:8000/api/status")
            .then(response => response.json())
            .then(data => {
                if (!Array.isArray(data)) return;

                let done = 0;

                data.forEach(job => {
                    let row = document.getElementById(`row${job.id}`);
                    
                    if (!row) {
                        row = document.createElement("tr");
                        row.id = `row${job.id}`;

                        const cell3 = document.createElement("td");
                        cell3.textContent = job.response_file;

                        const cell1 = document.createElement("td");
                        cell1.innerHTML = `
                            <div id="myProgress${job.id}" class="myProgress">
                                <div id="myBar${job.id}" class="myBar">0%</div>
                            </div>
                        `;

                        const cell2 = document.createElement("td");
                        cell2.innerHTML = `
                            <button id="downloadBtn${job.id}" class="downloadBtn" disabled>Ergebnis herunterladen</button>
                        `;

                        row.appendChild(cell3);
                        row.appendChild(cell1);
                        row.appendChild(cell2);
                        table.appendChild(row);
                        table.style.display = "block";
                    }

                    const prozent = Math.round((job.verarbeitet / job.gesamt) * 100);
                    const element = document.querySelector(`#myBar${job.id}`);
                    const bar = document.querySelector(`#myProgress${job.id}`);
                    const btn = document.querySelector(`#downloadBtn${job.id}`);

                    if (element) {
                        element.style.width = prozent + "%";
                        element.textContent = prozent + "%";
                    }

                    if (bar) {
                        bar.style.display = "block";
                    }

                    if (btn && job.status === "bereit") {
                        btn.disabled = false;
                        btn.onclick = () => downloadFile(job.id, btn);
                        done++;
                    }
                });

                if (done === data.length && data.length > 0) {
                    clearInterval(interval);
                }
            })
            .catch(error => console.error("Status-Abfrage fehlgeschlagen:", error));
    }, 1000);
});

function downloadFile(jobid, buttonElement){
  const bar = document.querySelector(`#row${jobid}`);
  fetch(`http://localhost:8000/api/download/${jobid}`)
    .then(response => {
      if (!response.ok) {
        throw new Error("Download fehlgeschlagen.");
      }
      return response.blob();
    })
    .then(blob => {
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "ergebnis_pdfs.zip";
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);
      buttonElement.disabled = true;
      if (bar) bar.remove();
    })
    .catch(error => {
      if (error.status === 404) {
        alert("Die Datei ist nicht mehr vorhanden.");
        if (bar) bar.remove();
      } else {
        alert("Datei konnte nicht heruntergeladen werden.");
      }
    });
}



  submitBtn2.addEventListener('click', () => {
    const file = document.querySelector("#page2 .drop-zone").file;
  
    if (file && (file.type === "application/pdf" || file.name.toLowerCase().endsWith(".pdf"))) {
      const formData = new FormData();
      formData.append("file", file);
  
      fetch("http://localhost:8000/api/metadata", {
        method: "POST",
        headers: {
          "Accept": "application/json"
        },
        body: formData
      })
      .then(response => {
        if (!response.ok) throw new Error("Fehler beim Hochladen");
        return response.json();
      })
      .then(data => {
        const element = document.querySelector("#page2result");
        element.style.display = "block";
        element.textContent = `Metadaten der Datei "${file.name}" (${file.type || 'Unbekannter Typ'}):\n\n${JSON.stringify(data, null, 2)}`;
      })
      .catch(error => {
        console.error("Upload fehlgeschlagen:", error);
      });
  
    } else {
      alert("Bitte wählen Sie eine PDF-Datei aus, um fortzufahren.");
    }
  });