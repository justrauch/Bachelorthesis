sudo service docker start
docker build -t pdf-zip-api . && docker run -p 8000:8000 pdf-zip-api
curl -X POST "http://localhost:8004/api/process-zip"      -H "
accept: application/zip"      -H "Content-Type: multipart/form-data"      -F "file=@Bsp_pdfs.zip"      --output ergebnis
_pdfs.zip
