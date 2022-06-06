#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly list is a palindrome
 * @head: the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = NULL, *e = NULL, *old_e = NULL;

	if (!head)
		return (1);

	s = *head;

	while (s != old_e)
	{
		e = s;
		while (e->next != old_e)
			e = e->next;
		if (s->n != e->n)
			return (0);
		s = s->next;
		old_e = e;
	}

	return (1);
}
