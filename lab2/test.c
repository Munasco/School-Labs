#include "lab2.h"
#include "test.h"

/* Given two arrays of length n, return 1 if both arrays contain the same 
 * elements. Return 0 otherwise. */
int check_equality(float arr1[], float arr2[], int n) {
    for (int i = 0; i < n; i++) {
        if (arr1[i] != arr2[i]) return 0;
    }
    return 1;
}

void test_get_parent_value() {
    float input[3] = {15, 8, 13};
    float answer = 15;
    float output = get_parent_value(input, 3, 1);

    printf("test_get_parent_value: ");

    if (output == answer) printf("PASSED\n");
    else printf("FAILED\n");
}

void test_get_left_value() {
    float input[3] = {15, 8, 13};
    float answer = 8;
    float output = get_left_value(input, 3, 0);

    printf("test_get_left_value: ");

    if (output == answer) printf("PASSED\n");
    else printf("FAILED\n");
}

void test_get_right_value() {
    float input[3] = {15, 8, 13};
    float answer = 13;
    float output = get_right_value(input, 3, 0);

    printf("test_get_right_value: ");

    if (output == answer) printf("PASSED\n");
    else printf("FAILED\n");
}

void test_is_max_heap() {
    float input1[3] = {8, 15, 13};
    float input2[3] = {15, 8, 13};
    float output1 = is_max_heap(input1, 3);
    float output2 = is_max_heap(input2, 3);

    printf("test_is_max_heap (first test case): ");
    if (output1 == 0) printf("PASSED\n");
    else printf("FAILED\n");

    printf("test_is_max_heap (second test case): ");
    if (output2 == 1) printf("PASSED\n");
    else printf("FAILED\n");
}

void test_heapify() {
    float input[3] = {8, 15, 13};
    float answer1[3] = {15, 8, 13};
    float answer2[3] = {15, 13, 8}; /* note there are two correct answers */

    heapify(input, 3);

    printf("test_heapify: ");
    if (check_equality(input, answer1, 3) || check_equality(input, answer2, 3))
        printf("PASSED\n");
    else printf("FAILED\n");
}

void test_heapsort() {
    float input[3] = {15, 8, 13};
    float answer[3] = {8, 13, 15};

    heapsort(input, 3);

    printf("test_heapsort: ");
    if (check_equality(input, answer, 3))
        printf("PASSED\n");
    else printf("FAILED\n");
}

void test_find_most_common_element() {
    float input[6] = {7, 3, 10, 7, 3, 9};
    float answer1 = 7;
    float answer2 = 3;

    float output = find_most_common_element(input, 6);

    printf("test_find_most_common_element: ");
    if (output == answer1 || output == answer2) printf("PASSED\n");
    else printf("FAILED\n");
}
