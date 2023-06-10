;;;; ${project-name}.lisp

(defpackage #:${project}
  (:documentation
   "${project-description}")
  (:use #:cl
	#:arrows)
  (:export #:main))
(in-package #:${project})

(defun main (&rest argv)
  (->> argv
       (format t "hello world, args: ~{~A~^, ~}~%")))
