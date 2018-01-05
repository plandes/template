#set($package = $group + "." + $artifact)
#set($package = $package.replace("-", ""))
package ${package};

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class HelloWorld {
    private static final Log log = LogFactory.getLog(HelloWorld.class);

    public static void main(String[] args) throws Exception {
	if (log.isInfoEnabled()) {
	    log.info("starting main...");
	}
	System.out.println("hello world!");
    }
}
