#ifndef LAB2_H
#define LAB2_H
#include <stdio.h>

void print_tree(float arr[], int n);
float get_parent_value(float arr[], int n, int index);
float get_left_value(float arr[], int n, int index);
float get_right_value(float arr[], int n, int index);
int is_max_heap(float arr[], int n);
void heapify(float arr[], int n);
void heapsort(float arr[], int n);
float find_most_common_element(float arr[], int n);

#endif
