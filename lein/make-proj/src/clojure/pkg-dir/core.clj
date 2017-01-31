(ns ${package}.core
  (:require [zensols.actioncli.log4j2 :as lu]
            [zensols.actioncli.parse :as cli])
  (:require [${package}.version :as ver])
  (:gen-class :main true))

(defn- version-info []
  (println (format "%s (%s)" ver/version ver/gitref)))

(defn- create-action-context []
  (cli/multi-action-context
   '((:repl zensols.actioncli.repl repl-command)
     (:hello ${package}.hello-world hello-world-command))
   :version-option (cli/version-option version-info)))

(defn -main [& args]
  (lu/configure "${artifact}-log4j2.xml")
  (cli/set-program-name "${artifact}")
  (-> (create-action-context)
      (cli/process-arguments args)))
