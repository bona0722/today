#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#define THREAD_NUM 1

//Task function prototypes. 
static void *disp_time(void* arg) {
	time_t rawt;
	struct tm *t;
	while(1){
		time(&rawt);
		t = localtime(&rawt);
		printf("Time: %02d:%02d:%02d\r", t->tm_hour, t->tm_min, t->tm_sec);
		fflush(stdout);
	}
}
//----------------------------------------------------------
int main( void )
{
	pthread_t thread_t;
	char c;
	
	printf("Hojung So 201801902\n");
	printf("Press any key and Enter to quit the program.... \n");
	fflush(stdout);
	

	if(pthread_create(&thread_t, NULL, disp_time, NULL) < 0) {
		printf("Error:was failed to create thread.");
	}

	scanf("%c", &c);
	fflush(stdout);
	printf("Bye~\n");
	
	return 0;
}

