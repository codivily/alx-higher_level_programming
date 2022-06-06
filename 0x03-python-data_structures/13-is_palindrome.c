#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - checks if a singly list is a palindrome
 * @head: the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = NULL, *e = NULL, *old_e = NULL;

	if (head == NULL)
	{
		perror("Not a list\n");
		exit(1);
	}
	s = *head;
	while (s != e)
	{
		e = s;
		while (e->next != old_e)
			e = e->next;
		if (s->n != e->n)
			return (0);
		old_e = e;
		s = s->next;
	}
	return (1);
}
