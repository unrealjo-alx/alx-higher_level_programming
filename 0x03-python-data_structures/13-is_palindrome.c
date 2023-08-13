#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list of integers is a palindrome.
 *
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);

	int length = 0;
	listint_t *ptr1 = *head;
	listint_t *ptr2 = *head;
	listint_t *temp = *head;

	/* Find the length of the list */
	while (temp != NULL)
	{
		temp = temp->next;
		length++;
	}

	/* Check if the length is odd */
	if (length % 2 != 0)
		return (0);

	int middle = length / 2;

	/* Move ptr2 to the middle of the list */
	while (ptr2->next != NULL && length != middle)
	{
		ptr2 = ptr2->next;
		length--;
	}

	ptr2 = reverseList(ptr2);

	/* Compare nodes in the first half with reversed nodes in the second half */
	while (ptr2 != NULL && ptr1 != NULL)
	{
		if (ptr2->n != ptr1->n)
			return (0);
		ptr2 = ptr2->next;
		ptr1 = ptr1->next;
	}

	return (1);
}
/**
 * reverseList - Reverses a singly linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
