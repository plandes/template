package com.zensols.app

import com.typesafe.scalalogging._
import org.slf4j.LoggerFactory

/**
  * Main entry point of the program.
  * @author Paul Landes
  */
object MainApp extends App {
  private val logger = Logger(LoggerFactory.getLogger(this.getClass))

  def main = {
    prinltn("hello world")
  }

  main
}
