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

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}

	current = *head;
	while (current != NULL)
	{
		if (current == *head && current->n > number)
		{
			new_node->next = current;
			*head = new_node;
			break;
		}

		if (current->next == NULL)
		{
			current->next = new_node;
			break;
		}

		if (current->n <= number && current->next->n >= number)
		{
			temp = current->next;
			current->next = new_node;
			new_node->next = temp;
			break;
		}
		current = current->next;
	}

	return (*head);
}
