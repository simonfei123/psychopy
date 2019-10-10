import sys
from psychopy.alerts._alerts import alert, AlertEntry, alertLog
from psychopy.alerts._errorHandler import ErrorHandler


class TestErrorHandler():
    """A class for testing the error handler"""

    def setup(self):
        # Set ErrorHandler
        self.error = ErrorHandler()
        sys.stderr = self.error

    def teardown(self):
        sys.stderr = sys.__stderr__
        alertLog.clear()

    def test_errorhandler(self):
        """Test error handler attributes"""
        assert (hasattr(self.error, "receiveAlert"))
        assert (hasattr(self.error, "alerts"))
        assert (hasattr(self.error, "errors"))
        assert (self.error.alerts == [])

    def test_errorhandler_flush(self):
        """Test flushing of alert to alertLog and clearing attributes"""
        alert(9999, self)
        assert (isinstance(self.error.alerts[-1], AlertEntry))
        sys.stderr.flush()
        assert (isinstance(alertLog.current[-1], AlertEntry))
        assert (sys.stderr.alerts == [])
