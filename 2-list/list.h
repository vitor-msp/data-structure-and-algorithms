#define MAX_LIST_ELEMENTS 10

#define getType(var, type) \
    type = 'u';            \
    switch (sizeof(var))   \
    {                      \
    case 1: /*character*/  \
        type = 'c';        \
        break;             \
    case 2:                \
    case 4: /*integer*/    \
        type = 'i';        \
        break;             \
    case 8: /*double*/     \
        type = 'd';        \
        break;             \
    default: /*undefined*/ \
        type = 'u';        \
    }

typedef struct list_t
{
    void *_elements[MAX_LIST_ELEMENTS];
    char _types[MAX_LIST_ELEMENTS];
    int _currLength;
    void *(*append)(void *list, void *itemValue, char itemType);
    void *(*print)(void *list);
    void *(*insert)(void *list, void *itemValue, char itemType, int pos);
    void *(*_shiftRight)(void *list, int initPos);
    void *(*pop)(void *list);
    void *(*_shiftLeft)(void *list, int initPos);
    void *(*delete)(void *list, int pos);
    void *(*clear)(void *list);
    int (*_isFull)(void *list);
    int (*_isEmpty)(void *list);
} List;