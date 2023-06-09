#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *curr = slow;
	listint_t *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t *left = *head;
	listint_t *right = prev;

	while (right != NULL)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}

	return (1);
}
