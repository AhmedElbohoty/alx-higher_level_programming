#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - if a singly linked list is a palindrome
 *
 * Return: - 0 if it is not a palindrome.
 *         - 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    int len = listint_len(*head);

    return (is_palindrome_helper(*head, len - 1));
}

/**
 * is_palindrome_helper - recursive helper for is_palindrome
 *
 * Return: - 0 if it is not a palindrome.
 *         - 1 if it is a palindrome.
 */
int is_palindrome_helper(listint_t *head, int end)
{
    int value_1, value_2;

    if (end <= 0)
        return (1);

    value_1 = head->n;
    value_2 = get_nodeint_at_index(head, end)->n;
    if (value_1 != value_2)
        return (0);

    head = (head)->next;

    return (is_palindrome_helper(head, end - 2));
}

/**
 * listint_len - returns the number of elements in a linked listint_t list
 * @h: singly linked list
 *
 * Return: The number of nodes
 */
size_t listint_len(const listint_t *h)
{
    size_t len = 0;
    const listint_t *temp = NULL;

    temp = h;
    while (temp != NULL)
    {
        temp = temp->next;
        len++;
    }

    return (len);
}

/**
 * get_nodeint_at_index - returns the nth node of a listint_t linked list.
 * @head: pointer of pointer to singly linked list
 * @index: the index of the node, starting at 0
 *
 * Return: - If success, return the nth node of a listint_t linked list.
 *         - If node doesn't exist, return NULL
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
    unsigned int len = 0;
    listint_t *temp;

    temp = head;
    while (temp != NULL && len != index)
    {
        temp = temp->next;
        len++;
    }

    if (temp == NULL)
        return (NULL);

    return (temp);
}
