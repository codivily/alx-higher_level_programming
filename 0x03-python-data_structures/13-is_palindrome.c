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
	listint_t *s = NULL, *e = NULL, *mid = NULL, *tmp = NULL;
	size_t count = 0, half = 0, i = 0;

	tmp = *head;
	while (tmp)
	{
		count++;
		tmp = tmp->next;
	}
	half = count / 2;
	mid = *head;
	while (i != half)
	{
		mid = mid->next;
		i++;
	}
	s = *head;
	while (s != mid)
	{
		tmp = e;
		e = mid;
		while (e->next != tmp)
			e = e->next;
		if (s->n != e->n)
			return (0);
		s = s->next;
	}
	return (1);
}
