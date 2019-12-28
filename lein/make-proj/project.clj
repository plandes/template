#set($package-dir = $package.replace(".", "/").replace("-", "_"))
(defproject ${group}/${artifact} "0.1.0-SNAPSHOT"
  :description "${project-description}"
  :url "https://github.com/${user}/${project}"
  :license {:name "MIT"
            :url "https://opensource.org/licenses/MIT"
            :distribution :repo}
  :plugins [[lein-codox "0.10.3"]
            [lein-javadoc "0.3.0"]
            [org.clojars.cvillecsteele/lein-git-version "1.2.7"]]
  :codox {:metadata {:doc/format :markdown}
          :project {:name "${project-name}"}
          :output-path "target/doc/codox"
          :source-uri "https://github.com/${user}/${project}/blob/v{version}/{filepath}#L{line}"}
  :javadoc-opts {:package-names ["${group}.${artifact}"]
                 :output-dir "target/doc/apidocs"}
  :git-version {:root-ns "${package}"
                :path "src/clojure/${package-dir}"
                :version-cmd "git describe --match v*.* --abbrev=4 --dirty=-dirty"}
  :source-paths ["src/clojure"]
  :test-paths ["test" "test-resources"]
  :java-source-paths ["src/java"]
  :javac-options ["-Xlint:unchecked"]
  :jar-exclusions [#".gitignore"]
  :dependencies [[org.clojure/clojure "1.9.0"]

                 ;; logging for core
                 [org.apache.logging.log4j/log4j-core "2.7"]

                 ;; command line
                 [com.zensols.tools/actioncli "0.0.30"]]
  :pom-plugins [[org.codehaus.mojo/appassembler-maven-plugin "1.6"
                 {:configuration ([:programs
                                   [:program
                                    ([:mainClass "${package}.core"]
                                     [:id "${app-name}"])]]
                                  [:environmentSetupFileName "setupenv"])}]]
  :profiles {:uberjar {:aot [${package}.core]}
             :appassem {:aot :all}
             :snapshot {:git-version {:version-cmd "echo -snapshot"}}
             :dev
             {:exclusions [org.slf4j/slf4j-log4j12
                           log4j/log4j
                           ch.qos.logback/logback-classic]
              :dependencies [[org.apache.logging.log4j/log4j-slf4j-impl "2.7"]
                             [org.apache.logging.log4j/log4j-1.2-api "2.7"]
                             [org.apache.logging.log4j/log4j-jcl "2.7"]
                             [org.apache.logging.log4j/log4j-jul "2.7"]]}
             :test {:jvm-opts ["-Dlog4j.configurationFile=test-resources/test-log4j2.xml"]}}
  :main ${package}.core)
