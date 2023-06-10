;;;; ${project}.asd

(asdf:defsystem #:${project}
  :description "${project-description}"
  :author "${user-name} <${user-email}>"
  :license "MIT"
  :version "0.1.0"
  :depends-on ("arrows")
  :serial t
  :pathname #P"src/"
  :components ((:file "${initial-package}"))
  :in-order-to ((test-op (test-op "${project}/test"))))

(asdf:defsystem #:${project}/test
  :description "Unit tests for the ${project} library."
  :author "Paul Landes <landes@mailc.net>"
  :license "MIT"
  :depends-on ("arrows"
	       "fiveam"
	       "${project}")
  :serial t
  :pathname #P"test/"
  :components ((:file "test"))
  :perform (test-op (op c)
                    (symbol-call :fiveam :run!
                                 (find-symbol* :${project} :${project}/test))))
