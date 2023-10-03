#include "lists.h"
/**
 * check_cycle - checks for  cycles in a linked-list
 * @head:  head of a linked-list to check for cycles
 * Return: (0) if no cycle or (1) if any cycle found
 */
int check_cycle(listint_t *head)
{
	listint_t *pre, *now = head;
	int idx, nod = 0;
	
	while (now && ++nod)
	{
		now = now->next;
		pre = head;
		idx = 0;
		while (now != pre && ++idx)
			pre = pre->next;
		if (idx < nod)
			return (1);
	}
	return (0);
}
