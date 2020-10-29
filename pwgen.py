"""Glue script to stand in until able to get C to copy to windows system
clipboard."""
import  win32clipboard as w32cb
import subprocess
import argparse
import sys

def copy_to_clipboard(string: str):
    """Copy string to windows clipboard using pywin32."""
    w32cb.OpenClipboard()
    w32cb.EmptyClipboard()
    w32cb.SetClipboardText(string)
    w32cb.CloseClipboard()

def in_pyinstaller():
    """Return True if running in Pyinstaller bundle, else False."""
    return (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'))

    # TODO needed? Pyinstaller-ness affects what this script would be called
    #   as but may not affect anything the script does internally.

def get_password(length):
    """Get password from a C subprocess."""
    command = f"c_pwgen {length}"
    completed_subproc = subprocess.run(command, capture_output=True)
    return completed_subproc.stdout

def main():
    print(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument("length",
                        type=int,
                        help="Number of characters to use in password")
    args = parser.parse_args()
    length = args.length
    password = get_password(length)[:-2] # TODO hacky fix--it comes back from C with
                            # \r\n chars on the end of it
    copy_to_clipboard(password)
    
    assert len(password) == length

if __name__ == '__main__':
    main()
    
    
