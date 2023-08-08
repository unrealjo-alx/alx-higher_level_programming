#include "lists.h"
/**
 * insert_node - Inserts a new node into a sorted linked list.
 *
 * @head: Pointer to the head of the linked list.
 * @number: Integer value to be inserted into the linked list.
 *
 * Return: Pointer to the newly inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (current == NULL || current->n > number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
