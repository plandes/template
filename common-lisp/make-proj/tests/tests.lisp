(defpackage #:${project}/tests
  (:use #:cl
	#:arrows
	#:fiveam
	#:${project}))
(in-package :${project}/tests)

(defvar test-resource-path
  (asdf:system-relative-pathname :${project} #p"tests/test-resource.txt"))

(def-suite ${project})
(in-suite ${project})

(defun read-file (infile)
  (with-open-file (instream infile :direction :input :if-does-not-exist nil)
    (when instream 
      (let ((string (make-string (file-length instream))))
        (read-sequence string instream)
        string))))

(test file-resource
  (is (equal "A dummy file."
	     (->> (read-file test-resource-path)
		  (string-trim '(#\Newline))))))
