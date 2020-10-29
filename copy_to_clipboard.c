# include <stdio.h>
# include <string.h>

# include "Windows.h"
# include "winuser.h"  /* https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-openclipboard 
						says header should be "winuser.h (include Windows.h)" */
# include "direct.h"
# include "winbase.h"

int main() {
	const char *output = "copied by C program";
	const size_t length = lstrlenA(output) + 1;
	//const size_t length = strlen(output) + 1;
	HGLOBAL hGlobal = GlobalAlloc(GMEM_MOVEABLE, length);
	memcpy(GlobalLock(hGlobal), output, length);
	GlobalUnlock(hGlobal);
	//HWND hWnd; /* "window handle"...saw one CPP example that initialized it without ever declaring a value. */
	OpenClipboard(NULL);
	EmptyClipboard();
	SetClipboardData(CF_TEXT, hGlobal);
	CloseClipboard();
}