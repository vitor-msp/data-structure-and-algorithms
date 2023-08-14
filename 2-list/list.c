#include <stdlib.h>
#include <stdio.h>
#include "./list.h"

void *print(void *list)
{
    printf("[");
    for (int index = 0; index < ((List *)list)->_currLength; index++)
    {
        switch (((List *)list)->_types[index])
        {
        case 'c': // character
            char *cPtr = (char *)((List *)list)->_elements[index];
            printf("%c ", *cPtr);
            break;
        case 'i': // integer
            int *iPtr = (int *)((List *)list)->_elements[index];
            printf("%i ", *iPtr);
            break;
        case 'd': // double
            double *dPtr = (double *)((List *)list)->_elements[index];
            printf("%f ", *dPtr);
            break;
        case 's': // string
            char **sPtr = (char **)((List *)list)->_elements[index];
            printf("%s ", sPtr);
            break;
        case 'j': // integer array
            int *jPtr = ((List *)list)->_elements[index];
            printf("[");
            for (int subIndex = 0; subIndex < MAX_LIST_ELEMENTS; subIndex++)
            {
                printf("%i ", jPtr[subIndex]);
            }
            printf("]");
            break;
        case 'e': // double array
            double *ePtr = ((List *)list)->_elements[index];
            printf("[");
            for (int subIndex = 0; subIndex < MAX_LIST_ELEMENTS; subIndex++)
            {
                printf("%f ", ePtr[subIndex]);
            }
            printf("]");
            break;
        case 'l': // another list
            printf("[");
            List *subList = ((List *)list)->_elements[index];
            subList->print(subList);
            printf("]");
            break;
        default:
            break;
        }
    }
    printf("]");
}

int _isFull(void *list)
{
    return ((List *)list)->_currLength >= MAX_LIST_ELEMENTS;
}

int _isEmpty(void *list)
{
    return ((List *)list)->_currLength <= 0;
}

void *append(void *list, void *itemValue, char itemType)
{
    if (((List *)list)->_isFull(list))
        return;
    int pos = ((List *)list)->_currLength++;
    ((List *)list)->_elements[pos] = itemValue;
    ((List *)list)->_types[pos] = itemType;
}

void *_shiftRight(void *list, int initPos)
{
    for (int index = (((List *)list)->_currLength - 1); index >= initPos; index--)
    {
        int nextIndex = index + 1;
        void *valuePtr = (void *)((List *)list)->_elements[index];
        ((List *)list)->_elements[nextIndex] = valuePtr;
        char type = ((List *)list)->_types[index];
        ((List *)list)->_types[nextIndex] = type;
    }
}

void *insert(void *list, void *itemValue, char itemType, int pos)
{
    if (((List *)list)->_isFull(list))
        return;
    ((List *)list)->_shiftRight(list, pos);
    ((List *)list)->_elements[pos] = itemValue;
    ((List *)list)->_types[pos] = itemType;
    ((List *)list)->_currLength++;
}

void *pop(void *list)
{
    if (((List *)list)->_isEmpty(list))
        return;
    int lastPos = ((List *)list)->_currLength - 1;
    void *element = ((List *)list)->_elements[lastPos];
    ((List *)list)->_elements[lastPos] = NULL;
    ((List *)list)->_types[lastPos] = NULL;
    ((List *)list)->_currLength--;
    return element;
}

void *_shiftLeft(void *list, int initPos)
{
    for (int index = initPos; index < (((List *)list)->_currLength - 1); index++)
    {
        int nextIndex = index + 1;
        void *valuePtr = (void *)((List *)list)->_elements[nextIndex];
        ((List *)list)->_elements[index] = valuePtr;
        char type = ((List *)list)->_types[nextIndex];
        ((List *)list)->_types[index] = type;
    }
}

void *delete(void *list, int pos)
{
    if (((List *)list)->_isEmpty(list))
        return;
    void *element = ((List *)list)->_elements[pos];
    ((List *)list)->_shiftLeft(list, pos);
    int lastPos = ((List *)list)->_currLength - 1;
    ((List *)list)->_elements[lastPos] = NULL;
    ((List *)list)->_types[lastPos] = NULL;
    ((List *)list)->_currLength--;
    return element;
}

void *clear(void *list)
{
    for (int index = 0; index < ((List *)list)->_currLength; index++)
    {
        ((List *)list)->_elements[index] = NULL;
        ((List *)list)->_types[index] = NULL;
    }
}

List newList()
{
    List list;
    list._currLength = 0;
    for (int index = 0; index < MAX_LIST_ELEMENTS; index++)
    {
        list._elements[index] = NULL;
        list._types[index] = NULL;
    }
    list.append = &append;
    list.insert = &insert;
    list._shiftRight = &_shiftRight;
    list.print = &print;
    list.pop = &pop;
    list._shiftLeft = &_shiftLeft;
    list.delete = &delete;
    list.clear = &clear;
    list._isEmpty = &_isEmpty;
    list._isFull = &_isFull;
    return list;
}

void main()
{
    List list = newList();
    char itemType;
    void *element;

    printf("=========== APPEND ===========\n");
    int val1 = 9;
    getType(val1, itemType);
    list.append(&list, &val1, itemType);
    list.print(&list);
    printf("\n");

    int val2 = 2;
    getType(val2, itemType);
    list.append(&list, &val2, itemType);
    list.print(&list);
    printf("\n");

    double val3 = 3.14;
    getType(val3, itemType);
    list.append(&list, &val3, itemType);
    list.print(&list);
    printf("\n");

    char val4 = 'a';
    getType(val4, itemType);
    list.append(&list, &val4, itemType);
    list.print(&list);
    printf("\n");

    char val5[4] = "text";
    list.append(&list, &val5, 's');
    list.print(&list);
    printf("\n");

    int val6[MAX_LIST_ELEMENTS] = {0};
    val6[0] = 10;
    val6[1] = 15;
    list.append(&list, &val6, 'j');
    list.print(&list);
    printf("\n");

    double val7[MAX_LIST_ELEMENTS] = {0};
    val7[0] = 0.5;
    val7[1] = 1.5;
    list.append(&list, &val7, 'e');
    list.print(&list);
    printf("\n");

    List sublist = newList();
    int val_1 = 7;
    sublist.append(&sublist, &val_1, 'i');
    char val_2 = 'b';
    sublist.append(&sublist, &val_2, 'c');
    list.append(&list, &sublist, 'l');
    list.print(&list);
    printf("\n");

    printf("=========== INSERT ===========\n");
    int val9 = 51;
    list.insert(&list, &val9, 'i', 2);
    list.print(&list);
    printf("\n");

    char val10 = 'z';
    list.insert(&list, &val10, 'c', 0);
    list.print(&list);
    printf("\n");

    printf("=========== NOT APPEND ===========\n");
    char val11 = 'N';
    list.append(&list, &val11, 'c');
    list.print(&list);
    printf("\n");

    printf("=========== NOT INSERT ===========\n");
    list.insert(&list, &val11, 'c', 0);
    list.print(&list);
    printf("\n");

    printf("=========== POP ===========\n");
    element = list.pop(&list);
    printf("%p\n", element);
    list.print(&list);
    printf("\n");

    element = list.pop(&list);
    printf("%p\n", element);
    list.print(&list);
    printf("\n");

    printf("=========== DELETE ===========\n");
    element = list.delete(&list, 4);
    printf("%f\n", *((double *)element));
    list.print(&list);
    printf("\n");

    list.delete(&list, 6);
    printf("%p\n", element);
    list.print(&list);
    printf("\n");

    printf("=========== CLEAR ===========\n");
    list.clear(&list);
    list.print(&list);
    printf("\n");

    printf("=========== NOT POP ===========\n");
    element = list.pop(&list);
    printf("%p\n", element);
    list.print(&list);
    printf("\n");

    printf("=========== NOT DELETE ===========\n");
    element = list.delete(&list, 3);
    printf("%p\n", element);
    list.print(&list);
    printf("\n");
}