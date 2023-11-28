#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of singly linked list
 * @number: the integer
 *
 * Return: - If failed, returns NULL
 *         - Else, retunrs pointer to the head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp;
	listint_t *new_node;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	current = *head;
	while (current != NULL)
	{
		if (current->n <= number && current->next->n >= number)
		{
			temp = current->next;
			current->next = new_node;
			new_node->n = number;
			new_node->next = temp;
			break;
		}
		current = current->next;
	}

	return (current);
}
