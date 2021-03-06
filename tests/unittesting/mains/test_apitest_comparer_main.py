import sys
import pytest

from aiotasks.__main__ import main


def test_aiotasks___main__runs_ok():
    # This test checks that the main command line run well
    
    sys.argv = [sys.argv[0], "-h"]
    
    with pytest.raises(SystemExit) as e:
        main()
        
    assert str(e.value) == '0'
