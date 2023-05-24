;;;; ${project}.asd

(asdf:defsystem #:${project}
  :description "${project-description}"
  :author "${user-name} <${user-email}>"
  :license "MIT"
  :version "0.1.0"
  :depends-on ("arrows")
  :pathname #P"src/"
  :components ((:file "${project-name}"))
  :in-order-to ((test-op (test-op "${project}/tests"))))

(asdf:defsystem #:${project}/tests
  :description "Unit tests for the ${project} library."
  :author "Paul Landes <landes@mailc.net>"
  :license "MIT"
  :depends-on ("arrows"
	       "fiveam"
	       "${project}")
  :pathname #P"test/"
  :components ((:file "test"))
  :perform (test-op (op c)
                    (symbol-call :fiveam :run!
                                 (find-symbol* :${project} :${project}/test))))
