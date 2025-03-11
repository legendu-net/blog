Status: published
Date: 2025-03-06 08:18:50
Modified: 2025-03-10 23:05:15
Author: Benjamin Du
Slug: editing-pdf-files-using-stirling-pdf
Title: Editing PDF Files Using Stirling-PDF
Category: Computer Science
Tags: Computer Science, PDF, editing, Stirling-PDF

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

It is recommended that you use Stirling-PDF via Docker.

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
  stirlingtools/stirling-pdf:latest-fat
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
  stirlingtools/stirling-pdf:latest-fat
```

## References

- [Stirling-PDF @ GitHub](https://github.com/Stirling-Tools/Stirling-PDF)

