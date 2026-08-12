---
title: Quickly Create a Scala Project Using Gradle in IntelliJ IDEA
created: '2019-01-26T18:11:29-08:00'
date: '2026-08-11T22:19:16-07:00'
authors:
  - bendu
label: quickly-create-a-scala-project-using-gradle-in-intellij-idea
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - Gradle
  - IntelliJ IDEA
  - JVM
---

## Easy Way

1. Create a directory (e.g., `demo_proj`) for your project.

1. Run `gradle init --type scala-library` in terminal in the above directory.

1. Import the directory as a Gradle project in IntelliJ IDEA.
   Alternatively,
   you can add `apply plugin: 'idea'` into `build.gradle`
   and then run the command `./gradlew openIdea` to import the directory as a Gradle project in Intellij IDEA.

## Hard Way

1. Create a Gradle project in IntelliJ IDEA.

1. Create a directory named `scala` under `src/main`.

1. Mark the directory `src/main/scala` as source root directory.

1. Open `build.gradle` and change its content to the following.

   ```
    plugins {
        id 'scala'
    }
    apply plugin: 'idea'

    group 'net.legendu'
    version '1.0-SNAPSHOT'

    sourceCompatibility = 1.8

    dependencies {
        // Use Scala 2.12 in our library project
        implementation 'org.scala-lang:scala-library:2.12.7'

        // Use Scalatest for testing our library
        testImplementation 'junit:junit:4.12'
        testImplementation 'org.scalatest:scalatest_2.12:3.0.5'

        // Need scala-xml at test runtime
        testRuntimeOnly 'org.scala-lang.modules:scala-xml_2.12:1.1.1'
    }
   ```
