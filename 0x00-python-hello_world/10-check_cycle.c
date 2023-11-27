#include <stdio.h>
#include "lists.h"

/*
 * check_cycle: checks if a singly linked list has a cycle in it
 * list: pointer to the singly linked list
 *
 * Return: - If the singly linked list has cycle, returns 1.
 *         - Else, returns 0.
 */
int check_cycle(listint_t *list)
{
	if (list->next == NULL)
		return (0);

	while (list != NULL)
	{
		if (list->count == 1)
			return (1);

		list->count = 1;
		list = list->next;
	}

	return (0);
}
