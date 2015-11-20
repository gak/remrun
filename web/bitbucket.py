def should_run_bitbucket(request, run):
    data = request.data

    try:
        repository = data['repository']['name']
    except KeyError:
        return False, 'Request did not have repository/name: {}'.format(data)

    try:
        ref_changes = data['refChanges']
    except KeyError:
        return False, 'Request did not have refChanges: {}'.format(data)

    if run.repository != repository:
        return False, 'Repository did not match "{}" != "{}"'.format(
            run.repository, repository,
        )

    does_it, reason = does_branch_appear(run, ref_changes)
    if not does_it:
        return does_it, reason

    return True, None


def does_branch_appear(run, ref_changes):
    saw = []
    for ref_change in ref_changes:
        branch = ref_change['ref_id'].split('/')[-1]
        saw.append(branch)
        if branch == run.branch:
            return True, None

    return False, \
        'No matching branches in refChanges. Wanted: {} Saw: {}'.format(
            run.branch, ','.join(saw)
        )
