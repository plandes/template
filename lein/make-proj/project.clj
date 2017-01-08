(defproject ${sub-group}/${group} "0.1.0-SNAPSHOT"
  :description "${project-description}"
  :url "https://github.com/${user}/${project-name}"
  :license {:name "Apache License version 2.0"
            :url "https://www.apache.org/licenses/LICENSE-2.0"
            :distribution :repo}
  :plugins [[lein-codox "0.10.1"]
            [org.clojars.cvillecsteele/lein-git-version "1.0.3"]]
  :codox {:metadata {:doc/format :markdown}
          :project {:name "${project-name}"}
          :output-path "target/doc/codox"
          :source-uri "https://github.com/${user}/${project}/blob/v{version}/{filepath}#L{line}"}
  :source-paths ["src/clojure"]
  :java-source-paths ["src/java"]
  :javac-options ["-Xlint:unchecked"]
  :jar-exclusions [#".gitignore"]
  :dependencies [[org.clojure/clojure "1.8.0"]

                 ;; command line
                 [com.zensols.tools/actioncli "0.0.12"]]
  :pom-plugins [[org.codehaus.mojo/appassembler-maven-plugin "1.6"
                 {:configuration ([:programs
                                   [:program
                                    ([:mainClass "${package}.core"]
                                     [:id "${app-name}"])]]
                                  [:environmentSetupFileName "setupenv"])}]]
  :profiles {:uberjar {:aot [${package}.core]}
             :appassem {:aot :all}
             :dev
             {:jvm-opts ["-Dlog4j.configurationFile=test-resources/log4j2.xml" "-Xms4g" "-Xmx12g" "-XX:+UseConcMarkSweepGC"]
              :exclusions [org.slf4j/slf4j-log4j12
                           ch.qos.logback/logback-classic]
              :dependencies [[org.apache.logging.log4j/log4j-core "2.7"]
                             [org.apache.logging.log4j/log4j-slf4j-impl "2.7"]
                             [org.apache.logging.log4j/log4j-jcl "2.7"]
                             [com.zensols/clj-append "1.0.5"]]}}
  :main ${package}.core)
