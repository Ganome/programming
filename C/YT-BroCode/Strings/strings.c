#include <stdio.h>
#include <string.h>

int main() {

  /*  Strings are character arrays  */
  char name[100];

  printf("\n\n\tPlease enter your name: \n");
  fgets(name, 100, stdin);
  name[strlen(name)-1] = '\0'; //  This removes the newline character at the end of 'name' variable

  printf("\n\nHello %s!\n\n", name);

  return 0;
}
