#include "lists.h"
#include <stddef.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: the list
 *
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = NULL, *curr = list;
	size_t curr_i = 0, i = 0;

	while (curr)
	{
		tmp = list;
		i = 0;
		while (tmp != curr)
		{
			tmp = tmp->next;
			i++;
		}
		if (curr_i != i)
			return (1);
		curr = curr->next;
		curr_i++;
	}
	return (0);
}
