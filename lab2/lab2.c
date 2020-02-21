#include "lab2.h"
#include<math.h>
#include<string.h>
#include<stdlib.h>
#define max(a, b) (((a) > (b)) ? (a): (b))


int left_index(char *source, char *search){
	char *new = strstr(source, search);
	return (new-source) ;
}
int right_index(char *source, char *search){
	char *new = strstr(source, search);

	int x = (new -source);
	return strlen(search)+ x;
}




void print_tree(float arr[], int n) {
    /* Your code goes here */
    int length = n;

char bleet[length][600]; 
char * rege = "leret";
char ter[40] ;
strncpy(bleet[2], rege+2,3);
// printf("%s", bleet[2]);

int last_row = (int)(1 + floor(log2(length)));
int last_index = (int) pow(2, last_row-1)-1;

strcpy(bleet[0], ""); 
for(int i = last_index; i<length; i++){
	int len = strlen(bleet[0]);
	sprintf(bleet[0]+ len, "%g    ", arr[i]);
}

int k = 1;
while(last_index > 0){
length = last_index;
last_row = (int)(1 + floor(log2(length)));
last_index = (int)pow(2, last_row-1)-1;
strcpy(bleet[k], ""); 
int temp = 0;
int leap = 0;
for (int j = last_index; j < length; j++){
	char temporary[9];
    char left_value[8];
	char right_value[8];
	gcvt(arr[2*j+1], 6, left_value);
    left_value[strlen(left_value)-1] = '\0';
	gcvt(arr[2*j+2], 6, right_value);
    right_value[strlen(right_value) - 1] = '\0';
	int len = &bleet[k-1][left_index(bleet[k-1] + leap, right_value)] - &bleet[k-1][right_index(bleet[k-1]+ leap,left_value)];
	int new_place = len%2 == 0 ? len/2: (len+1)/2;
	
	new_place = new_place + right_index(bleet[k-1] + leap,left_value) - temp;
	gcvt(arr[j], 10, temporary);
    temp = strlen(temporary) -1;
	for(int i = 0; i < new_place-1; i++) strcat(bleet[k], " ");
	leap = strlen(bleet[k]);
	sprintf(bleet[k]+leap, "%g", arr[j]);	
//	printf("%d ", leap);
}
k++;
}

for (int i = k-1; i > -1; i--){
	printf("%s\n", bleet[i]);
}

}

float get_parent_value(float arr[], int n, int index) {
    /* Your code goes here */
    return arr[(int) floor((index-1)/2)];
}

float get_left_value(float arr[], int n, int index) {
    /* Your code goes here */
    return arr[2*index + 1];
}

float get_right_value(float arr[], int n, int index) {
    /* Your code goes here */
    return arr[2*index + 2];
}

int is_max_heap(float arr[], int n) {
    /* Your code goes here */
    for (int i = n-1; i> 0; i--){
        if (arr[i] > get_parent_value(arr, n, i))
            return 0; 
    }
    return 1;
}

void heapify(float arr[], int n) {
    /* Your code goes here */
    int last= n-1;
    int next = (int)floor(n/2);
    for (int j = next-1; j>-1; j--)
    {int left_index = 2*j+1;
    int right_index = 2*j+2;
    float max_child;
    int swap_index;
    while(right_index <= last || left_index <= last)
    {
        if(right_index <= last){
             max_child = max(arr[left_index], arr[right_index]);
            swap_index = arr[left_index] == max_child ? left_index : right_index;
        }
        else{
            swap_index  = left_index;
            max_child = arr[left_index];
        }
        if (arr[j] < max_child){
            float temp = arr[j];
            arr[j] = max_child;
            arr[swap_index] = temp;
        }
        else break;
    }
}
}
void heapsort(float arr[], int n) {
    /* Your code goes here */
    int size_heap = n;
    while (size_heap){ 
        float temp = arr[0];
        arr[0] = arr[size_heap - 1];
        arr[size_heap - 1] = temp;
        size_heap--;
        int curr_index = 0; 
        int left_index = 1;
        int right_index = 2; 
        int last_index = size_heap - 1;
        while (right_index <= last_index || left_index <= last_index){
            float max_child;
            int swap_index;
            if (right_index <= last_index){
                max_child = max(arr[left_index], arr[right_index]);
                swap_index = arr[left_index] == max_child ? left_index : right_index;
            }
            else{
                max_child = arr[left_index];
                swap_index = left_index;
            }
            if (arr[curr_index] < max_child){
                float temp = arr[curr_index];
                arr[curr_index] = arr[swap_index];
                arr[swap_index] = temp; 
                curr_index = swap_index;
                left_index = 2*curr_index + 1;
                right_index = 2*curr_index + 2;
            }
            else break;
        }
    }
}

float find_most_common_element(float arr[], int n) {
    /* Your code goes here */
    float mostelement = arr[0];
    int arrcount = 0;
    for(int i = 0; i< n; i++){
        int count = 0;
        for (int j = 0; j < n; j++){
            if(arr[j] == arr[i]) count++;
        }
        if(arrcount < count) {
            arrcount = count;
            mostelement = arr[i];
        } 
    }
    return mostelement;
}
