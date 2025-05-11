Status: published
Date: 2025-03-06 08:18:50
Modified: 2025-05-11 16:45:21
Author: Benjamin Du
Slug: editing-pdf-files-using-stirling-pdf
Title: Editing PDF Files Using Stirling-PDF
Category: Computer Science
Tags: Computer Science, PDF, editing, Stirling-PDF

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You can try Stirling-PDF at 
<https://stirlingpdf.io/>
.

## Start a Stirling-PDF Service Using Docker

The following command starts a (local) service of Stirling-PDF at the port 6000.
```
docker run -d \
  --name stirling-pdf \
  -p 6000:8080 \
  -v "./StirlingPDF/trainingData:/usr/share/tessdata" \
  -v "./StirlingPDF/extraConfigs:/configs" \
  -v "./StirlingPDF/customFiles:/customFiles/" \
  -v "./StirlingPDF/logs:/logs/" \
  -v "./StirlingPDF/pipeline:/pipeline/" \
  -e DOCKER_ENABLE_SECURITY=false \
  -e LANGS=en_GB \
  stirlingtools/stirling-pdf:latest
```
Use the following command if you'd like to enable security and login.
```
docker run -d \
  --name stirling-pdf \
  -p 6000:8080 \
  -v "./StirlingPDF/trainingData:/usr/share/tessdata" \
  -v "./StirlingPDF/extraConfigs:/configs" \
  -v "./StirlingPDF/customFiles:/customFiles/" \
  -v "./StirlingPDF/logs:/logs/" \
  -v "./StirlingPDF/pipeline:/pipeline/" \
  -e DOCKER_ENABLE_SECURITY=true \
  -e SECURITY_ENABLE_LOGIN=true \
  -e LANGS=en_GB \
  stirlingtools/stirling-pdf:latest
```

Notice that there's also the Docker image 
`stirlingtools/stirling-pdf:latest-fat` (with more fonts, etc) that you can use.

## References

- [Stirling-PDF @ GitHub](https://github.com/Stirling-Tools/Stirling-PDF)

