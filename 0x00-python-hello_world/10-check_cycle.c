#include "lists.h"
/**
 * check_cycle - checks if a linked-list
 *               contains a cycle or not
 *
 * @head: head of a linked-list to check
 * Return: (0) if  no cycle found
 *         (1) if any cycle found
 */
int check_cycle(listint_t *head)
{
	listint_t *pre, *now;
	int idx, nod;

	now = head;
	nod = 0;
	while (now)
	{
		now = now->next;
		pre = head;
		nod++;
		idx = 0;
		while (idx < nod)
		{
			if (now == pre)
				return (1);
			pre = pre->next;
			idx++;
		}
	}
	return (0);
}
