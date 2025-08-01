// Elementreferenzen
const dropZone = document.getElementById('dropZone');
const submitBtn1 = document.getElementById('submitBtn1');
const submitBtn2 = document.getElementById('submitBtn2');
const submitBtn3 = document.getElementById('submitBtn3');

// Seitenumschalter (zeigt nur die gewählte Seite an, startet Job-Status-Abfrage auf Seite 2)
function switchsite(page) {
    for (let i = 1; i <= 3; i++) {
        const tmp = document.getElementById('page' + i);
        tmp.style.display = (i === page) ? 'block' : 'none';
        if (i === 3) {
            document.getElementById("submitBtn3").click(); // Startet Statusüberwachung bei Seite 2
        }
    }
}

// Aktiviert Upload-Button nur, wenn mind. eine Datei vorhanden ist
function enableButtonIfFilesPresent(dropZone, count) {
    const button = dropZone.parentElement.querySelector('button');
    if (button) {
        button.disabled = count === 0;
    }
}

// Zeigt ausgewählte Datei in der Drop-Zone an
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

// Drag-and-Drop- und Klick-Handling für Drop-Zonen
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

    // Klick öffnet Dateiauswahl-Dialog
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

// Submit ZIP: Hochladen und Verarbeitung starten
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
            headers: { "Accept": "application/zip" },
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
            switchsite(3); // Wechsle zur Statusseite
        })
        .catch(error => console.error("Status-Abfrage fehlgeschlagen:", error));
    } else {
        alert("Bitte wählen Sie eine ZIP-Datei aus, um fortzufahren.");
    }
});

// Statusseite: wiederholt Status jedes Jobs abfragen und Fortschritt anzeigen
submitBtn3.addEventListener('click', () => {
    submitBtn3.style.display = "none";

    const table = document.getElementById("page3table");
    let interval = setInterval(() => {
        fetch("http://localhost:8000/api/status")
            .then(response => response.json())
            .then(data => {
                if (!Array.isArray(data)) return;

                let last = false;
                if (data.length <= 0) last = true;

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
                            <button id="downloadBtn${job.id}" class="downloadBtn" disabled style="display: none;">Ergebnis herunterladen</button>
                            <button id="stopBtn${job.id}" class="stopBtn">Verarbeitung stoppen</button>
                        `;

                        row.appendChild(cell3);
                        row.appendChild(cell1);
                        row.appendChild(cell2);
                        table.appendChild(row);
                        table.style.display = "block";
                    }

                    // Fortschrittsbalken aktualisieren
                    const prozent = Math.round((job.verarbeitet / job.gesamt) * 100);
                    const element = document.querySelector(`#myBar${job.id}`);
                    const bar = document.querySelector(`#myProgress${job.id}`);
                    const dbtn = document.querySelector(`#downloadBtn${job.id}`);
                    const sbtn = document.querySelector(`#stopBtn${job.id}`);

                    if (element && job.status != "fehlgeschlagen") {
                        element.style.width = prozent + "%";
                        element.textContent = prozent + "%";
                    } else {
                        element.style.width = "100%";
                        element.textContent = `Bearbeitung fehlgeschlagen bei ${prozent} %`;
                    }

                    if (bar) {
                        bar.style.display = "block";
                    }

                    // Job stoppen (nur wenn aktiv)
                    if (sbtn && job.status === "in_bearbeitung") {
                        sbtn.onclick = () => stopJob(job.id, sbtn);
                        dbtn.disabled = false;
                    }

                    // Download-Link aktivieren, wenn Job fertig oder fehlgeschlagen
                    if (dbtn && (job.status === "bereit" || job.status === "fehlgeschlagen")) {
                        dbtn.onclick = () => downloadFile(job, dbtn);
                        dbtn.style.display = "block";
                        sbtn.style.display = "none";
                        dbtn.disabled = false;
                    }
                });

                if (last) clearInterval(interval); // Beende Statusabfrage, wenn keine aktiven Jobs mehr
            })
            .catch(error => console.error("Status-Abfrage fehlgeschlagen:", error));
    }, 3000);
});

// Datei herunterladen
function downloadFile(job, buttonElement) {
  const jobid = job.id;
  const bar = document.querySelector(`#row${jobid}`);
  if (buttonElement) buttonElement.disabled = true;

  fetch(`http://localhost:8000/api/download/${jobid}`)
    .then(response => {
      if (!response.ok) {
        const err = new Error("Download fehlgeschlagen.");
        err.status = response.status;
        throw err;
      }
      let filename = `ergebnis_${job.response_file}`;
      if (!filename.toLowerCase().endsWith(".zip")) filename += ".zip";
      return response.blob().then(blob => ({ blob, filename }));
    })
    .then(({ blob, filename }) => {
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
      if (buttonElement) buttonElement.disabled = true;
    })
    .catch(error => {
      console.error("Download-Fehler:", error);
      if (buttonElement) buttonElement.disabled = false;
      alert(error.status === 404
        ? "Die Datei ist nicht mehr vorhanden."
        : error.status === 403
          ? "Die Datei wird noch bearbeitet. Bitte später erneut versuchen."
          : "Datei konnte nicht heruntergeladen werden.");
    });
}

// Fortschrittszeile entfernen
function remove_bar(bar) {
    if (bar) bar.remove();

    const table = document.getElementById("page3table");
    const rowCount = table.children.length;
    if (rowCount === 1) {
        table.style.display = "none";
    }
}

// Verarbeitung eines Jobs abbrechen
function stopJob(jobid, buttonElement) {
    const bar = document.querySelector(`#row${jobid}`);
    fetch(`http://localhost:8000/api/stop/${jobid}`)
        .then(response => response.json())
        .then(() => {
            buttonElement.disabled = true;
        })
        .catch(error => {
            console.error("Fehler beim Stoppen des Jobs:", error);
            alert("Verarbeitung konnte nicht gestoppt werden.");
        });
}

// PDF-Datei hochladen zur Extraktion von Metadaten (Seite 3)
submitBtn2.addEventListener('click', () => {
    const file = document.querySelector("#page2 .drop-zone").file;

    if (file && (file.type === "application/pdf" || file.name.toLowerCase().endsWith(".pdf"))) {
        const formData = new FormData();
        formData.append("file", file);

        fetch("http://localhost:8000/api/metadata", {
            method: "POST",
            headers: { "Accept": "application/json" },
            body: formData
        })
        .then(response => {
            if (!response.ok) throw new Error("Fehler beim Hochladen");
            return response.json();
        })
        .then(data => {
            const element = document.querySelector("#page2result");
            element.style.display = "block";
            element.innerHTML = `Metadaten der Datei "${file.name}" (${file.type || 'Unbekannter Typ'}):\n\n${JSON.stringify(data, null, 2).replace(/\n/g, "<br>")}`;
        })
        .catch(error => {
            console.error("Upload fehlgeschlagen:", error);
        });
    } else {
        alert("Bitte wählen Sie eine PDF-Datei aus, um fortzufahren.");
    }
});
