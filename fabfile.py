from fabric.api import *
import datetime
env.hosts = ['jamiecurle.com']
env.user = 'jcurle'
from settings import DATABASES


env.production_uploads = 'designcc@backup1.designcc.co.uk:/home/designcc/backups/tass/uploads'

env.production_db_name = 'jamiecurle2'
env.production_db_user = 'jamiecurle2'

env.production_backup_path = '/home/jcurle/backups'
env.production_backup_name = '%s.dump.sql.gz' % env.production_db_name


def dump_and_get_production_db():
    # dump the production database, download it, then delete it
    mysqldump = run('cd backups/ && mysqldump -u %s %s | gzip >  %s%s' % (env.production_db_name, env.production_db_user, env.production_backup_path, env.production_backup_name) )
    download_dump = get('%s%s' % (env.production_backup_path, env.production_backup_name) ,  env.production_backup_name )
    deletedump = run('rm %s%s' % (env.production_backup_path, env.production_backup_name))


def backup_local_dev_database():
    #   backup the old database - no need to be brutal and drop it
    dump_file = '%(NAME)s_local_dump.sql' % DATABASES['default']
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_db = '%s_%s' % (DATABASES['default']['NAME'], timestamp)
    
    dump_current_db = local('mysqldump %s > %s' % (DATABASES['default']['NAME'], dump_file) )
    create_the_old_db = local('echo "CREATE DATABASE %s CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql' % backup_db )
    import_old_db = local('mysql %s < %s ' % (backup_db, dump_file) )
    drop_database = local('mysqladmin drop  %s ' % DATABASES['default']['NAME'])
    delete_dump = local('rm %s' %  dump_file )    
    

def create_new_dev_database():
    dump_file = env.production_backup_name.replace('.gz', '')
    create_the_new_db = local('echo "CREATE DATABASE %s CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql' % DATABASES['default']['NAME'] )
    gunzip = local('gunzip %s' % env.production_backup_name)
    import_production_dump = local('mysql %s < %s ' % (DATABASES['default']['NAME'], dump_file) )
    delete_dump = local('rm %s' %  dump_file )

def get_latest_production_db():
    dump_and_get_production_db()
    backup_local_dev_database()
    create_new_dev_database()

def update_local_media():
    local('rsync  -e ssh -rav jcurle@jamiecurle.com:/home/jcurle/sites/jamiecurle/uploads media')


def update_local():
    update_local_media()
    get_latest_production_db()













def d():
    run('cd sites/jamiecurle/jamiecurle/; git pull origin master')
    run('supervisorctl restart jamiecurle')


def deploy():
    local('git commit -a')
    local('git push origin master')
    run('cd sites/jamiecurle/jamiecurle/; git pull origin master')
    run('supervisorctl restart jamiecurle')

