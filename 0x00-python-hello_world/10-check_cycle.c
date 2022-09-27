#include "lists.h"

/**
 * check_cycle- a function that checks for a cycle in a linked list
 * @list: pointer to the linked list head
 * Return: 1 if there is a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
listint_t *temp1 = list, *temp2 = list;
while (temp2 && temp2->next)
{

temp1 = temp1->next;
temp2 = temp2->next->next;

if (temp1 == temp2)
{
return (1);
}

}
return (0);
}
