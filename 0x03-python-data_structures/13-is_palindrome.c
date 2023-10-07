#include <stdlib.h>
#include "lists.h"

#define INT_BUFF 12
int use_malloc(listint_t *head, listint_t *node, int len);

/**
 * is_palindrome - checks if a singly linked list is symetric
 * @head: pointer to the first node of the singly linked list
 * Return: (True / False) if the linked  list  is  palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *move, *node;
	int len = 0, arr[INT_BUFF];

	if (head == NULL)
		return (0);

	move = node = *head;
	while (move && node->next)
	{
		move = move->next->next;
		if (len < INT_BUFF)
			arr[len] = node->n;
		node = node->next;
		len++;
	}
	if (move)
		node = node->next;

	if (len >= INT_BUFF)
		return (use_malloc(*head, node, len));

	while (node && len)
	{
		len--;
		if (node->n != arr[len])
			return (0);
		node = node->next;
	}

	return (1);
}

/**
 * use_malloc - checks if a singly linked list is palindrome
 * @head: pointer to the first  node in the list
 * @node: pointer to the middle node in the list
 * @len: number of nodes between @head and @node
 *
 * Return: (True / False) if the linked  list  is palindrome
 */
int use_malloc(listint_t *head, listint_t *node, int len)
{
	int i = 0, *arr = malloc(sizeof(int) * (len + 1));

	while (i < len)
	{
		arr[i] = head->n;
		head = head->next;
		i++;
	}

	while (node && i)
	{
		i--;
		if (node->n != arr[i])
		{
			free(arr);
			return (0);
		}
		node = node->next;
	}

	free(arr);
	return (1);
}
