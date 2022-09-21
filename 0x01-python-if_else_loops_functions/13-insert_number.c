#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{

listint_t *temp, *new_node;


new_node = malloc(sizeof(listint_t));

if (new_node)
{
    temp = *head;
    new_node->n = number;

    if (*head == NULL)
    {
        *head = new_node;
        new_node->next = NULL;
        return (new_node);
    }

    *head = new_node;
    new_node->next = temp;
    return new_node;
}

return (NULL);
}