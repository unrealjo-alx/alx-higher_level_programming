#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (list == NULL)
		return (0);
	fast_ptr = list;

	/* Since fast_prt is faster, no neede to check for null slow_ptr */
	while (fast_ptr != NULL)
	{
		slow_ptr = fast_ptr;
		/*The first jump is necessary to surpass the slow pointer.*/
		fast_ptr = fast_ptr->next;
		while (fast_ptr != NULL && fast_ptr != slow_ptr)
			fast_ptr = fast_ptr->next;
		if (fast_ptr == slow_ptr)
			return (1);
	}

	return (0);
}
