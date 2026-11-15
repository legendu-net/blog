---
title: Exceptions in Java
created: '2012-11-04T09:54:41-08:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: exceptions-in-java
license: CC-BY-4.0
tags:
  - exception
  - programming
  - Java
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. You can suppress warnings of unchecked exceptions by using

   ```
    :::java
    SuppressWarnings("unchecked") 
   ```

   but generally speaking,
   you cannot suppress warnings of checked exceptions.

1. You can use more than one `catch` blocks if necessary
   but you can only catch one exception in a catch block before Java 7.
   Starting from Java 7,
   you can catch multiple exceptions in a catch block.
   For example,
   The old style Java code

   ```
    :::java
    } catch (FirstException ex) {
         logger.error(ex);
         throw ex;
    } catch (SecondException ex) {
         logger.error(ex);
         throw ex;
    }
   ```

   becomes

   ```
    :::java
    } catch (FirstException | SecondException ex) {
         logger.error(ex);
        throw ex;
    }
   ```

   in Java 7+.

1. To guarantee that some code will be run eventually,
   you have to put it into a `finally` block before Java 7.
   Starting from Java 7,
   filesystem resources are managed automatically
   so that you do not have to release them manually in a `finally` block.
   For example,
   old style Java code

   ```
    :::java
    BufferedReader br = new BufferedReader(new FileReader(path));
    try {
       return br.readLine();
    } finally {
       br.close();
    }
   ```

   becomes

   ```
    :::java
    try (BufferedReader br = new BufferedReader(new FileReader(path)) {
       return br.readLine();
    }
   ```

   in Java 7.
