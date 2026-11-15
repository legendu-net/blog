---
title: Check Whether an Email Address Is Valid in Java
created: '2012-05-12T23:58:54-07:00'
date: '2026-11-15T12:20:30-08:00'
authors:
  - bendu
label: check-whether-an-email-address-is-valid-in-java
license: CC-BY-4.0
tags:
  - pattern
  - match
  - Java
  - programming
  - email address
---

See the following code.

```Java
String email = "test@test.com";
Pattern p = Pattern.compile(".+@.+\\.[a-z]+");
Matcher m = p.matcher(email);
boolean matchFound = m.matches();
if(matchFound){
    System.out.println("EMAIL OK");
}else{
    System.out.println("EMAIL ERROR");
}
```
