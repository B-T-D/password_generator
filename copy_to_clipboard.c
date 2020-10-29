# include <stdio.h>
# include <string.h>

# include "Windows.h"
# include "winuser.h"
# include "direct.h"

int main() {
	const char *output = "copied by C program";
	const size_t length = strlen(output) + 1;
	HGLOBAL hMem = GlobalAlloc(GMEM_MOVEABLE, length);
	memcpy(GlobalLock(hMem), output, length);
	GlobalUnlock(hMem);
	OpenClipboard(0);
	EmptyClipboard();
	SetClipboardData(CF_TEXT, hMem);
	CloseClipboard();
}