# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define MAX_CHARS 94
# define DEFAULT_LENGTH 12
# define MAX_LENGTH 100

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
	size_t num_chars = strlen(characters);
	time_t t;
	srand((unsigned) time(&t));
	int choice_ind;
	/* Mod by len(characters) - 1, because appears rand() is inclusive of 
	RAND_MAX. E.g. modding by 26 would be 27 values total, [0..26] */
	
	for (int i=0; i<length; i++) {
		choice_ind = rand() % num_chars;
		char rand_char = characters[choice_ind];
		password[i] = rand_char;
	}
	password[length] = '\0';

}

void display_help()
	/* Print an output that mimicks output from python argparse --help [-h] flag. */
{
	printf("usage: pwgen [-h] length\n\n");
	printf("positional arguments:\n\tlength\t\t\tNumber of characters in password\n");
}
	
int main(int argc, char *argv[])
{	
	int length;
	if ((atoi(argv[1]) != DEFAULT_LENGTH) && (atoi(argv[1]) > 0)) {
		length = atoi(argv[1]);
	} else {
		length = DEFAULT_LENGTH;
	}
	//printf("generating pw of length %d\n", length);
		
	char characters[MAX_CHARS];
	int j = 0;
	for (int i=32; i<=126; i++) {
		characters[j] = i;
		j++;
	}
	char password[MAX_LENGTH]; /* TODO -- make it use length arg, may need an ifdef for windows.
									This here is temp to get it to compile with microsoft VS */
	generate_pw(length, characters, password);
	printf("%s\n", password);
	
}