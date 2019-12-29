#set($package = $group + "." + $artifact)
#set($package = $package.replace("-", ""))
package ${package};

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertFalse;

public class HelloWorldTest {
    private static final Log log = LogFactory.getLog(HelloWorldTest.class);

    @Before
    public void setup() {
	if (log.isDebugEnabled()) {
	    log.debug("setting up...");
	}
    }

    @After
    public void tearDown() {
	if (log.isDebugEnabled()) {
	    log.debug("tearing down...");
	}
    }

    @Test
    public void testHelloWorld() throws Exception {
        assertEquals(1, 1);
    }
}
