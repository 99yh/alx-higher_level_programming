#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is symetric
 * @head: pointer to the first node of the singly linked list
 * Return: (True / False) if the linked  list  is  palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int i, len = 0, *arr, flag = 0;

	if (head == NULL)
		return (0);

	node = *head;
	while (node && node->next && ++len)
		node = node->next->next;
	if (node)
		flag = 1;

	arr = malloc(sizeof(int) * (len + 1));
	i = 0;
	node = *head;
	while (i < len)
	{
		arr[i] = node->n;
		node = node->next;
		i++;
	}

	if (flag)
		node = node->next;
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
