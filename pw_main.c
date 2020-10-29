# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define MAX_CHARS 94
# define DEFAULT_LENGTH 12

/* Generate password of int length length using characters selected from 
	those in char *characters 
	
	Args:
		int length: Length of the password.
		char *characters: Pointer to an array of the character set to use.
		char *password: Empty, properly sized character array to hold the password.
	
	Returns:
		char * : Pointer to an array of the characters that make up the password.
*/
void generate_pw(int length, char *characters, char *password)
{
	//printf("characters are %s\n", characters);
	size_t num_chars = strlen(characters);
	//printf("num_chars is %d\n", num_chars);
	char c = *characters;
	char c2 = characters[1];
	//printf("character c = %d\n", (char) c);
	//printf("characters[1] = %c\n", c2);
	//printf("*characters = %s\n", *characters);
	//printf("characters is now %s\n", characters);
	time_t t;
	srand((unsigned) time(&t));
	int choice_ind;
	/* Mod by len(characters) - 1, because appears rand() is inclusive of 
	RAND_MAX. E.g. modding by 26 would be 27 values total, [0..26] */
		
	for (int i=0; i<=length; i++) {
		choice_ind = rand() % num_chars;
		char rand_char = characters[choice_ind];
		password[i] = rand_char;
	}
	printf("password now = %s\n", password);
	
	/* build the PW string here as a character array, then return a pointer to that same string */
}
		

int main(int argc, char *argv[])
{
	printf("from pw main: %s\n", argv[1]);
	int length = atoi(argv[1]);
	char characters[MAX_CHARS];
	int j = 0;
	for (int i=32; i<=126; i++) {
		characters[j] = i;
		j++;
	}
	char password[DEFAULT_LENGTH]; /* TODO -- make it use length arg, may need an ifdef for windows.
									This here is temp to get it to compile with microsoft VS */
	generate_pw(length, characters, password);
	printf("password from main: %s\n", password);
	
}