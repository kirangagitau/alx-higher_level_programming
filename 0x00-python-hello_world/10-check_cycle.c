#include <stdio.h>
#include "list.h"

/**
 * check_cycle - check if linked list has cycle
 * @list: thelist to be checked
 *
 * Return: 1 =cycle, 0=no cycle
 **/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0)
}
