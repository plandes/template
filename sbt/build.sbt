name := "hello-world"
organization := "com.zensols/hello-world"
version := "1.0"

scalaVersion := "2.11.8"
javacOptions ++= Seq("-source", "1.8", "-target", "1.8", "-Xlint")
scalacOptions := Seq("-target:jvm-1.8")

resolvers += Resolver.sonatypeRepo("public")

testOptions += Tests.Setup( cl =>
   cl.loadClass("org.slf4j.LoggerFactory").
     getMethod("getLogger",cl.loadClass("java.lang.String")).
     invoke(null,"ROOT")
)

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % "2.4.12",
  "com.typesafe.akka" %% "akka-stream" % "2.4.12",
  "com.typesafe.akka" %% "akka-stream-testkit" % "2.4.12",
  "com.typesafe.akka" %% "akka-testkit" % "2.4.12",
  "org.scalatest" %% "scalatest" % "3.0.0",
  "org.scalatest" %% "scalatest" % "3.0.0" % "test",
  "com.typesafe.scala-logging" %% "scala-logging" % "3.1.0",
  "org.apache.logging.log4j" % "log4j-core" % "2.7",
  "org.apache.logging.log4j" % "log4j-api" % "2.7",
  "org.apache.logging.log4j" % "log4j-slf4j-impl" % "2.7",
  "org.apache.logging.log4j" % "log4j-jcl" % "2.7",
  "org.scalaj" %% "scalaj-http" % "2.3.0"
)

dependencyOverrides += "joda-time" % "joda-time" % "2.8.2"

// (fset 'clojure-to-sbt-dep
//    [?\C-a ?\M-\\ ?  ?  ?\" ?\C-d ?\C-s ?/ left ?\C-d ?\" ?\S-  ?% ?% ?\S-  ?\" ?\C-s ?\" left ?\C-d ?% ?\S-  ?\" ?\C-e backspace ?,])
