# Dev Notes

## Architecture

 * celery worker with unique task queue name on each host, e.g. runrem-host1
 * rest api backend for executing commands
 * redis backend for celery
 * django orm for configuration
 
## Phase 1

 * Stack
   * Django
   * DRF 
   * Celery 
   * Redis
 * API/Configuration
   * basic endpoint (e.g. /api/run/basic/)
   * bitbucket enpoint (e.g. /api/run/bitbucket/)
   * bitbucket: repository and branch filters
   * apikey generated for each endpoint (e.g. /?apikey=a80f)
   * host, converting to a celery queue called "runrem-{host}"
   * user, e.g. puppet
   * command, e.g. git pull
   * directory, e.g. /etc/puppet/modules/
 * Django Admin, very basic--just for api configuration

## Phase 2

 * ?? 
